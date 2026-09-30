(function(){
var t=[].slice.call(document.querySelectorAll('button.gt')),lb=document.getElementById('lb'),v=document.getElementById('lbv'),cap=document.getElementById('lbc'),i=0,sx=0;
function show(n){i=(n+t.length)%t.length;var s=t[i].querySelector('video');v.poster=s.poster;v.src=window.clipSrc(s);v.setAttribute('aria-label',s.getAttribute('aria-label'));cap.textContent=s.getAttribute('aria-label');lb.hidden=false;document.body.classList.add('lock');var p=v.play();if(p&&p.catch)p.catch(function(){})}
function hide(){lb.hidden=true;v.pause();v.removeAttribute('src');v.load();document.body.classList.remove('lock')}
t.forEach(function(b,n){b.addEventListener('click',function(){show(n)})});
lb.querySelector('.lx').onclick=hide;lb.querySelector('.lp').onclick=function(){show(i-1)};lb.querySelector('.ln').onclick=function(){show(i+1)};
lb.addEventListener('click',function(e){if(e.target===lb)hide()});
lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
lb.addEventListener('touchend',function(e){var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>60)show(i+(dx<0?1:-1))});
document.addEventListener('keydown',function(e){if(lb.hidden)return;if(e.key==='Escape')hide();if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)});
})();
