(function(){
var t=[].slice.call(document.querySelectorAll('.gt')),lb=document.getElementById('lb'),im=document.getElementById('lbi'),cap=document.getElementById('lbc'),i=0,sx=0;
function show(n){i=(n+t.length)%t.length;var s=t[i].querySelector('img');im.src=s.src;im.alt=s.alt;cap.textContent=s.alt;lb.hidden=false;document.body.classList.add('lock')}
function hide(){lb.hidden=true;document.body.classList.remove('lock')}
t.forEach(function(b,n){b.addEventListener('click',function(){show(n)})});
lb.querySelector('.lx').onclick=hide;lb.querySelector('.lp').onclick=function(){show(i-1)};lb.querySelector('.ln').onclick=function(){show(i+1)};
lb.addEventListener('click',function(e){if(e.target===lb)hide()});
lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
lb.addEventListener('touchend',function(e){var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)show(i+(dx<0?1:-1))});
document.addEventListener('keydown',function(e){if(lb.hidden)return;if(e.key==='Escape')hide();if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)});
})();
