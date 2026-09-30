(function(){
var $=function(s){return document.querySelector(s)};
$('#yr').textContent=new Date().getFullYear();
// countdown to re-opening
var open=new Date('2026-10-01T09:00:00+01:00'),cd=$('#cd');
function tick(){var d=open-new Date();
 if(d<=0){cd.innerHTML='<p>We\'re OPEN — 10% off any hairstyle for 14 days! ✦</p>';return}
 var s=Math.floor(d/1e3),v=[[Math.floor(s/86400),'Days'],[Math.floor(s%86400/3600),'Hrs'],[Math.floor(s%3600/60),'Min'],[s%60,'Sec']];
 cd.innerHTML='<p>Opening in</p>'+v.map(function(x){return'<div><b>'+String(x[0]).padStart(2,'0')+'</b><small>'+x[1]+'</small></div>'}).join('')}
tick();setInterval(tick,1000);
// booking form
var date=$('#date'),time=$('#time'),today=new Date().toISOString().slice(0,10);
date.min=today>'2026-10-01'?today:'2026-10-01';
function slots(){var h=[];for(var m=9*60;m<=17*60;m+=30){var hh=Math.floor(m/60),mm=m%60;h.push((hh<10?'0':'')+hh+':'+(mm?'30':'00'))}return h}
slots().forEach(function(t){var o=document.createElement('option');o.textContent=t;time.appendChild(o)});
date.addEventListener('change',function(){var d=new Date(date.value+'T12:00:00'),s=d>=new Date('2026-10-01T00:00:00')&&d<=new Date('2026-10-14T23:59:59');$('#disc').checked=s});
$('#bf').addEventListener('submit',function(e){e.preventDefault();var f=e.target,v={},err=$('#err');
 ['name','phone','email','service','date','time','notes'].forEach(function(k){v[k]=(f[k].value||'').trim()});
 if(!v.name||!v.service||!v.date||!v.time){err.textContent='Please fill in your name, service, date and time.';return}
 if(!/^[\d\s+()-]{10,}$/.test(v.phone)){err.textContent='Please enter a valid phone number so we can confirm.';return}
 err.textContent='';
 var nice=new Date(v.date+'T12:00:00').toLocaleDateString('en-GB',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
 var body='New booking request\n\nName: '+v.name+'\nPhone: '+v.phone+'\nEmail: '+(v.email||'-')+'\nService: '+v.service+'\nDate: '+nice+'\nTime: '+v.time+'\nOpening 10% discount: '+($('#disc').checked?'Yes':'No')+'\nNotes: '+(v.notes||'-');
 var href='mailto:mariejaca@yahoo.com?subject='+encodeURIComponent('Booking request – '+v.service+' – '+nice)+'&body='+encodeURIComponent(body);
 $('#bf').hidden=true;$('#ok').hidden=false;$('#okmsg').textContent=v.name+', you\'ve requested '+v.service+' on '+nice+' at '+v.time+'.';
 $('#mailbtn').href=href;window.location.href=href;$('#ok').scrollIntoView({behavior:'smooth',block:'center'})});
})();
