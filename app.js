(function(){
var y=document.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
var cd=document.getElementById('cd');
if(cd){var open=new Date('2026-10-01T09:00:00+01:00'),end=new Date('2026-10-15T00:00:00+01:00');
 function tick(){var n=new Date(),d=open-n;
  if(n>=end){cd.innerHTML='<p>Thank you for celebrating with us!</p>';return}
  if(d<=0){cd.innerHTML='<p>We\'re open. 10% off is live now!</p>';return}
  var s=Math.floor(d/1e3),v=[[Math.floor(s/86400),'Days'],[Math.floor(s%86400/3600),'Hrs'],[Math.floor(s%3600/60),'Min'],[s%60,'Sec']];
  cd.innerHTML=v.map(function(x){return'<div><b>'+String(x[0]).padStart(2,'0')+'</b><small>'+x[1]+'</small></div>'}).join('')}
 tick();setInterval(tick,1000)}
window.mailForm=function(id,subject,keys,labels){
 var f=document.getElementById(id);if(!f)return;
 f.addEventListener('submit',function(e){e.preventDefault();var err=f.querySelector('.err'),v={};
  keys.forEach(function(k){v[k]=(f.elements[k].value||'').trim()});
  if(!v.name||(keys.indexOf('phone')>-1&&!/^[\d\s+()-]{10,}$/.test(v.phone||''))||(keys.indexOf('contact')>-1&&!v.contact)||(keys.indexOf('msg')>-1&&id==='msgf'&&!v.msg)){err.textContent='Please complete the required fields (name and a valid contact).';return}
  err.textContent='';
  var body=keys.map(function(k){return labels[k]+': '+(v[k]||'-')}).join('\n');
  window.location.href='mailto:mariejaca@yahoo.com?subject='+encodeURIComponent(subject+' - '+v.name)+'&body='+encodeURIComponent(body);
  err.style.color='#2e7d32';err.textContent='Your email app should open with your message ready to send.'})};
})();
