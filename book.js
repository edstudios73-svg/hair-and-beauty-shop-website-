(function(){
'use strict';
var $=function(s){return document.querySelector(s)},$$=function(s){return[].slice.call(document.querySelectorAll(s))};
var OPEN=new Date(2026,9,1),OFFER_END=new Date(2026,9,14),st={service:'',date:'',time:''};
var steps=$$('.bs'),go=$('#go'),err=$('#err'),df=$('#df');
function iso(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}
function parse(s){var p=s.split('-');return new Date(+p[0],+p[1]-1,+p[2])}
function nice(s){return parse(s).toLocaleDateString('en-GB',{weekday:'long',day:'numeric',month:'long',year:'numeric'})}
function inOffer(d){return d>=OPEN&&d<=OFFER_END}
function openStep(n,scroll){steps.forEach(function(s,i){s.classList.toggle('open',i===n)});if(scroll){var el=steps[n];setTimeout(function(){el.scrollIntoView({behavior:'smooth',block:'center'})},60)}}
function done(n,v){steps[n].classList.toggle('done',v)}
function sum(){
 var set=function(id,val,ph){var e=$(id);e.textContent=val||ph;e.classList.toggle('set',!!val)};
 set('#v-s',st.service,'Choose a service');set('#v-d',st.date&&nice(st.date),'Pick a date');set('#v-t',st.time,'Select a time');
 $('#v-o').hidden=!(st.date&&inOffer(parse(st.date)));go.disabled=!(st.service&&st.date&&st.time)}
/* services */
$$('.opt').forEach(function(o){o.addEventListener('click',function(){$$('.opt').forEach(function(x){x.classList.remove('sel')});o.classList.add('sel');st.service=o.dataset.v;done(0,true);sum();openStep(1,true)})});
var qs=new URLSearchParams(location.search),pre=qs.get('service');
if(pre)$$('.opt').forEach(function(o){if(o.dataset.v===pre){st.service=pre;o.classList.add('sel');done(0,true);openStep(1)}});
/* calendar */
var today=new Date();today.setHours(0,0,0,0);var minD=today>OPEN?today:OPEN,view=new Date(minD.getFullYear(),minD.getMonth(),1),maxView=new Date(minD.getFullYear(),minD.getMonth()+3,1);
function cal(){
 $('#cmonth').textContent=view.toLocaleDateString('en-GB',{month:'long',year:'numeric'});
 $('#cprev').disabled=view<=new Date(minD.getFullYear(),minD.getMonth(),1);$('#cnext').disabled=view>=maxView;
 var first=new Date(view.getFullYear(),view.getMonth(),1),off=(first.getDay()+6)%7,days=new Date(view.getFullYear(),view.getMonth()+1,0).getDate(),h='';
 for(var i=0;i<off;i++)h+='<span></span>';
 for(var d=1;d<=days;d++){var dt=new Date(view.getFullYear(),view.getMonth(),d),s=iso(dt),dis=dt<minD;
  h+='<button type="button" class="cd2'+(inOffer(dt)?' off':'')+(s===st.date?' sel':'')+'" data-d="'+s+'"'+(dis?' disabled':'')+' aria-label="'+nice(s)+'">'+d+'</button>'}
 $('#cdays').innerHTML=h}
$('#cprev').onclick=function(){view=new Date(view.getFullYear(),view.getMonth()-1,1);cal()};
$('#cnext').onclick=function(){view=new Date(view.getFullYear(),view.getMonth()+1,1);cal()};
$('#cdays').addEventListener('click',function(e){var b=e.target.closest('.cd2');if(!b||b.disabled)return;st.date=b.dataset.d;cal();done(1,true);sum();openStep(2,true)});
if(qs.get('offer')&&!st.date){st.date=iso(minD<=OFFER_END?minD:OPEN);done(1,true)}
cal();
/* times */
var th='';for(var m=9*60;m<=17*60+30;m+=30){th+='<button type="button" class="tm">'+String(Math.floor(m/60)).padStart(2,'0')+':'+(m%60?'30':'00')+'</button>'}
$('#times').innerHTML=th;
$('#times').addEventListener('click',function(e){var b=e.target.closest('.tm');if(!b)return;$$('.tm').forEach(function(x){x.classList.remove('sel')});b.classList.add('sel');st.time=b.textContent;done(2,true);sum();openStep(3,true)});
/* step edit buttons */
steps.forEach(function(s,i){var e=s.querySelector('.edit');if(e)e.addEventListener('click',function(){openStep(i,true)})});
/* remembered details */
try{var sv=JSON.parse(localStorage.getItem('mhb')||'{}');['name','phone','email'].forEach(function(k){if(sv[k])df.elements[k].value=sv[k]})}catch(e){}
/* initial state */
if(st.service&&!st.date)openStep(1);sum();
/* submit */
go.addEventListener('click',function(){
 var v={name:df.elements.name.value.trim(),phone:df.elements.phone.value.trim(),email:df.elements.email.value.trim(),notes:df.elements.notes.value.trim()};
 if(!v.name){err.textContent='Please add your name in step 4.';openStep(3,true);return}
 if(!/^[\d\s+()-]{10,}$/.test(v.phone)){err.textContent='Please add a valid phone number so we can confirm.';openStep(3,true);return}
 if(v.email&&!/^\S+@\S+\.\S+$/.test(v.email)){err.textContent='That email address doesn\'t look right.';openStep(3,true);return}
 err.textContent='';
 if($('#rem').checked){try{localStorage.setItem('mhb',JSON.stringify({name:v.name,phone:v.phone,email:v.email}))}catch(e){}}
 var offer=inOffer(parse(st.date))?'Yes (10% opening discount)':'No';
 var body='New booking request\n\nName: '+v.name+'\nPhone: '+v.phone+'\nEmail: '+(v.email||'-')+'\nService: '+st.service+'\nDate: '+nice(st.date)+'\nTime: '+st.time+'\nOpening offer: '+offer+'\nNotes: '+(v.notes||'-');
 var href='mailto:mariejaca@yahoo.com?subject='+encodeURIComponent('Booking request: '+st.service+' - '+nice(st.date)+' '+st.time)+'&body='+encodeURIComponent(body);
 $('#dmsg').textContent='Thanks '+v.name.split(' ')[0]+'. Send the email to lock in your request. We\'ll confirm by phone or email.';
 $('#dsum').innerHTML=[['Service',st.service],['Date',nice(st.date)],['Time',st.time],['Offer',offer]].map(function(r){return'<div><dt>'+r[0]+'</dt><dd>'+r[1]+'</dd></div>'}).join('');
 $('#mailbtn').href=href;$('#done').hidden=false;document.body.classList.add('lock');setTimeout(function(){location.href=href},400);
 $('#icsbtn').onclick=function(){var p=st.date.replace(/-/g,''),hh=parseInt(st.time),mm=st.time.slice(3),z=function(n){return String(n).padStart(2,'0')},
  ics=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Maries Hair and Beauty//EN','BEGIN:VEVENT','UID:'+Date.now()+'@marieshairandbeauty','DTSTAMP:'+new Date().toISOString().replace(/[-:]/g,'').slice(0,15)+'Z','DTSTART;TZID=Europe/London:'+p+'T'+z(hh)+mm+'00','DTEND;TZID=Europe/London:'+p+'T'+z(hh+1)+mm+'00','SUMMARY:'+st.service+' at Marie\'s Hair & Beauty','LOCATION:48 Victoria Street\\, Wolverhampton WV1 3PJ','DESCRIPTION:Requested booking. Call 01902 471053 to change.','END:VEVENT','END:VCALENDAR'].join('\r\n'),
  a=document.createElement('a');a.href=URL.createObjectURL(new Blob([ics],{type:'text/calendar'}));a.download='maries-appointment.ics';a.click()}});
$('#done').addEventListener('click',function(e){if(e.target.id==='done'){this.hidden=true;document.body.classList.remove('lock')}});
})();
