(function(){
var $=function(s){return document.querySelector(s)},$$=function(s){return[].slice.call(document.querySelectorAll(s))};
var st={step:0,service:'',date:'',time:''},OPEN=new Date(2026,9,1),OFFER_END=new Date(2026,9,14);
var steps=$$('.step'),prog=$$('#prog li'),next=$('#next'),prev=$('#prev'),err=$('#err'),sum=$('#sum'),disc=$('#disc');
function iso(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}
function parse(s){var p=s.split('-');return new Date(+p[0],+p[1]-1,+p[2])}
function nice(s){return parse(s).toLocaleDateString('en-GB',{weekday:'long',day:'numeric',month:'long',year:'numeric'})}
function inOffer(d){return d>=OPEN&&d<=OFFER_END}
// service chips
$$('.chip').forEach(function(c){c.addEventListener('click',function(){$$('.chip').forEach(function(x){x.classList.remove('sel')});c.classList.add('sel');st.service=c.dataset.v;upd()})});
var q=new URLSearchParams(location.search),pre=q.get('service');
if(pre){$$('.chip').forEach(function(c){if(c.dataset.v===pre){c.click()}})}
// dates
var today=new Date();today.setHours(0,0,0,0);var start=today>OPEN?today:OPEN,ds=$('#dates');
for(var i=0;i<28;i++){var d=new Date(start.getFullYear(),start.getMonth(),start.getDate()+i),b=document.createElement('button');
 b.type='button';b.className='dt';b.dataset.d=iso(d);
 b.innerHTML=(inOffer(d)?'<span class="off">10% off</span>':'')+'<small>'+d.toLocaleDateString('en-GB',{weekday:'short'})+'</small><b>'+d.getDate()+'</b><em>'+d.toLocaleDateString('en-GB',{month:'short'})+'</em>';
 b.addEventListener('click',function(){$$('.dt').forEach(function(x){x.classList.remove('sel')});this.classList.add('sel');st.date=this.dataset.d;disc.checked=inOffer(parse(st.date));upd()});ds.appendChild(b)}
$('#dnote').textContent=today<OPEN?'Bookings open from Thursday 1 October 2026. Dates in the opening offer are marked.':'Dates in the opening offer are marked.';
// times
var ts=$('#times');for(var m=9*60;m<=17*60+30;m+=30){var t=String(Math.floor(m/60)).padStart(2,'0')+':'+(m%60?'30':'00'),tb=document.createElement('button');tb.type='button';tb.className='tm';tb.textContent=t;
 tb.addEventListener('click',function(){$$('.tm').forEach(function(x){x.classList.remove('sel')});this.classList.add('sel');st.time=this.textContent;upd()});ts.appendChild(tb)}
if(q.get('offer')){var o=$$('.dt')[0];if(o)o.click();}
// remembered details
var df=$('#df');try{var sv=JSON.parse(localStorage.getItem('mhb')||'{}');['name','phone','email'].forEach(function(k){if(sv[k])df.elements[k].value=sv[k]})}catch(e){}
function details(){return{name:df.elements.name.value.trim(),phone:df.elements.phone.value.trim(),email:df.elements.email.value.trim(),notes:df.elements.notes.value.trim()}}
function ok(){var s=st.step;if(s===0)return!!st.service;if(s===1)return!!st.date;if(s===2)return!!st.time;return true}
function render(){
 steps.forEach(function(e,i){e.classList.toggle('on',i===st.step)});
 prog.forEach(function(e,i){e.classList.toggle('on',i===st.step);e.classList.toggle('ok',i<st.step)});
 prev.hidden=st.step===0;next.textContent=st.step===3?'Request booking':'Continue';
 var rows=[];if(st.service)rows.push(['Service',st.service]);if(st.date)rows.push(['Date',nice(st.date)]);if(st.time)rows.push(['Time',st.time]);
 if(disc.checked&&st.date&&inOffer(parse(st.date)))rows.push(['Offer','10% opening discount']);
 sum.hidden=!rows.length||st.step===0;sum.innerHTML=rows.map(function(r){return'<div><span>'+r[0]+'</span><b>'+r[1]+'</b></div>'}).join('');
 next.disabled=!ok();err.textContent='';window.scrollTo({top:0,behavior:'smooth'})}
function upd(){next.disabled=!ok();var rows=[];if(st.service)rows.push(['Service',st.service]);if(st.date)rows.push(['Date',nice(st.date)]);if(st.time)rows.push(['Time',st.time]);
 sum.hidden=!rows.length||st.step===0;sum.innerHTML=rows.map(function(r){return'<div><span>'+r[0]+'</span><b>'+r[1]+'</b></div>'}).join('')}
prev.addEventListener('click',function(){if(st.step>0){st.step--;render()}});
next.addEventListener('click',function(){
 if(st.step<3){if(ok()){st.step++;render()}return}
 var v=details();
 if(!v.name){err.textContent='Please enter your name.';return}
 if(!/^[\d\s+()-]{10,}$/.test(v.phone)){err.textContent='Please enter a valid phone number so we can confirm your booking.';return}
 if(v.email&&!/^\S+@\S+\.\S+$/.test(v.email)){err.textContent='That email address doesn\'t look right.';return}
 if($('#rem').checked){try{localStorage.setItem('mhb',JSON.stringify({name:v.name,phone:v.phone,email:v.email}))}catch(e){}}
 var offer=disc.checked&&inOffer(parse(st.date))?'Yes (10% opening discount)':'No';
 var body='New booking request\n\nName: '+v.name+'\nPhone: '+v.phone+'\nEmail: '+(v.email||'-')+'\nService: '+st.service+'\nDate: '+nice(st.date)+'\nTime: '+st.time+'\nOpening offer: '+offer+'\nNotes: '+(v.notes||'-');
 var href='mailto:mariejaca@yahoo.com?subject='+encodeURIComponent('Booking request: '+st.service+' - '+nice(st.date)+' '+st.time)+'&body='+encodeURIComponent(body);
 $('#bk').classList.add('fin');$('#done').hidden=false;
 $('#dmsg').textContent='Thanks '+v.name.split(' ')[0]+'! Send the email to lock in your request. We\'ll confirm by phone or email.';
 $('#dsum').innerHTML=[['Service',st.service],['Date',nice(st.date)],['Time',st.time],['Offer',offer],['Phone',v.phone]].map(function(r){return'<div><span>'+r[0]+'</span><b>'+r[1]+'</b></div>'}).join('');
 $('#mailbtn').href=href;window.scrollTo({top:0});setTimeout(function(){window.location.href=href},350);
 $('#icsbtn').onclick=function(){var p=st.date.replace(/-/g,''),h=st.time.replace(':',''),dt=p+'T'+h+'00',dh=parseInt(st.time)+1,de=p+'T'+String(dh).padStart(2,'0')+st.time.slice(3)+'00';
  var ics=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Maries Hair and Beauty//EN','BEGIN:VEVENT','UID:'+Date.now()+'@marieshairandbeauty','DTSTAMP:'+new Date().toISOString().replace(/[-:]/g,'').slice(0,15)+'Z','DTSTART;TZID=Europe/London:'+dt,'DTEND;TZID=Europe/London:'+de,'SUMMARY:'+st.service+' at Marie\'s Hair & Beauty','LOCATION:48 Victoria Street\\, Wolverhampton WV1 3PJ','DESCRIPTION:Requested booking. Call 01902 471053 to change.','END:VEVENT','END:VCALENDAR'].join('\r\n');
  var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([ics],{type:'text/calendar'}));a.download='maries-appointment.ics';a.click()}});
disc.addEventListener('change',upd);
render();window.scrollTo(0,0);
})();
