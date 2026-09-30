(function(){
'use strict';
var d=document,de=d.documentElement,$=function(s,c){return(c||d).querySelector(s)},$$=function(s,c){return[].slice.call((c||d).querySelectorAll(s))};
var RM=matchMedia('(prefers-reduced-motion:reduce)').matches,FINE=matchMedia('(pointer:fine)').matches;
var y=$('#yr');if(y)y.textContent=new Date().getFullYear();

/* ---- split headlines into masked words ---- */
var wi=0;
function split(n){[].slice.call(n.childNodes).forEach(function(c){
 if(c.nodeType===3){var f=d.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(t){
  if(!t)return;if(/^\s+$/.test(t)){f.appendChild(d.createTextNode(' '));return}
  var o=d.createElement('span');o.className='sw';var i=d.createElement('span');i.textContent=t;i.style.setProperty('--w',wi++);o.appendChild(i);f.appendChild(o)});c.replaceWith(f)}
 else if(c.nodeType===1)split(c)})}
$$('[data-split]').forEach(function(h){wi=0;var lbl=h.textContent;h.setAttribute('aria-label',lbl);split(h);$$('.sw',h).forEach(function(s){s.setAttribute('aria-hidden','true')})});

/* ---- reveal on scroll ---- */
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.15,rootMargin:'0px 0px -6% 0px'});
$$('[data-r],[data-split]').forEach(function(e){io.observe(e)});
requestAnimationFrame(function(){$$('.hero [data-r],.phero [data-r],.hero [data-split],.phero [data-split]').forEach(function(e){e.classList.add('in')})});

/* ---- header: solid on scroll, hide on scroll down, progress bar ---- */
var hdr=$('#hdr'),bar=$('.prog'),lastY=0,statement=$('#statement'),words=[],parallax=$$('[data-speed]');
if(statement){statement.innerHTML=statement.textContent.trim().split(/\s+/).map(function(w){return'<span class="w">'+w+'</span>'}).join(' ');words=$$('.w',statement)}
var ticking=false;
function onScroll(){var sy=scrollY,h=de.scrollHeight-innerHeight;
 hdr.classList.toggle('solid',sy>40);hdr.classList.toggle('hide',sy>lastY+4&&sy>500&&!d.body.classList.contains('menu')||false);if(sy<lastY-4)hdr.classList.remove('hide');lastY=sy;
 bar.style.transform='scaleX('+(h>0?sy/h:0)+')';
 if(words.length){var r=statement.getBoundingClientRect(),p=(innerHeight*.82-r.top)/(r.height+innerHeight*.25);p=Math.max(0,Math.min(1,p));var n=Math.round(p*words.length);words.forEach(function(w,i){w.classList.toggle('on',i<n)})}
 if(!RM&&innerWidth>980)parallax.forEach(function(e){var r=e.parentNode.getBoundingClientRect();if(r.bottom<0||r.top>innerHeight)return;e.style.transform='translate3d(0,'+((r.top+r.height/2-innerHeight/2)*(+e.dataset.speed)/300)+'px,0)'});
 ticking=false}
addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});onScroll();

/* ---- mobile menu ---- */
var bg=$('#burger'),mn=$('#mnav');
function menu(o){d.body.classList.toggle('menu',o);d.body.classList.toggle('lock',o);bg.setAttribute('aria-expanded',o);mn.setAttribute('aria-hidden',!o)}
bg.addEventListener('click',function(){menu(!d.body.classList.contains('menu'))});
$$('a',mn).forEach(function(a){a.addEventListener('click',function(){menu(false)})});
addEventListener('keydown',function(e){if(e.key==='Escape')menu(false)});

/* ---- custom cursor, magnetic buttons, tilt (desktop only) ---- */
if(FINE&&!RM){
 var c=d.createElement('div');c.className='cur';c.innerHTML='<i class="r"></i><i class="d"></i>';d.body.appendChild(c);
 var dot=$('.d',c),ring=$('.r',c),mx=-100,my=-100,rx=-100,ry=-100;
 addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY;dot.style.transform='translate('+mx+'px,'+my+'px)'},{passive:true});
 (function loop(){rx+=(mx-rx)*.16;ry+=(my-ry)*.16;ring.style.transform='translate('+rx+'px,'+ry+'px)';requestAnimationFrame(loop)})();
 d.addEventListener('mouseover',function(e){c.classList.toggle('h',!!e.target.closest('a,button,[data-tilt],.rail'))});
 $$('[data-mag]').forEach(function(b){b.addEventListener('mousemove',function(e){var r=b.getBoundingClientRect();b.style.transform='translate('+((e.clientX-r.left-r.width/2)*.22)+'px,'+((e.clientY-r.top-r.height/2)*.3)+'px)'});b.addEventListener('mouseleave',function(){b.style.transform=''})});
 $$('[data-tilt]').forEach(function(t){t.addEventListener('mousemove',function(e){var r=t.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,yy=(e.clientY-r.top)/r.height-.5;t.style.transform='perspective(800px) rotateY('+(x*10)+'deg) rotateX('+(-yy*10)+'deg) translateZ(0)'});t.addEventListener('mouseleave',function(){t.style.transform=''})});
}

/* ---- drag-to-scroll rail ---- */
var rail=$('#rail');
if(rail){var down=false,sx=0,sl=0,moved=false;
 rail.addEventListener('mousedown',function(e){down=true;moved=false;sx=e.pageX;sl=rail.scrollLeft;rail.classList.add('drag')});
 addEventListener('mouseup',function(){down=false;rail.classList.remove('drag')});
 addEventListener('mousemove',function(e){if(!down)return;var dx=e.pageX-sx;if(Math.abs(dx)>4)moved=true;rail.scrollLeft=sl-dx});
 rail.addEventListener('click',function(e){if(moved){e.preventDefault();e.stopPropagation()}},true);
 rail.addEventListener('keydown',function(e){if(e.key==='ArrowRight')rail.scrollBy({left:320,behavior:'smooth'});if(e.key==='ArrowLeft')rail.scrollBy({left:-320,behavior:'smooth'})})}

/* ---- countdown ---- */
var cd=$('#cd');
if(cd){var open=new Date('2026-10-01T09:00:00+01:00'),end=new Date('2026-10-15T00:00:00+01:00');
 (function tick(){var n=new Date(),dd=open-n;
  if(n>=end){cd.innerHTML='<p>Thank you for celebrating with us.</p>';return}
  if(dd<=0){cd.innerHTML='<p>We\'re open. 10% off is live now.</p>';setTimeout(tick,60000);return}
  var s=Math.floor(dd/1e3),v=[[Math.floor(s/86400),'Days'],[Math.floor(s%86400/3600),'Hours'],[Math.floor(s%3600/60),'Mins'],[s%60,'Secs']];
  cd.innerHTML=v.map(function(x){return'<div><b>'+String(x[0]).padStart(2,'0')+'</b><small>'+x[1]+'</small></div>'}).join('');setTimeout(tick,1000)})()}

/* ---- mailto forms ---- */
window.mailForm=function(id,subject,keys,labels){
 var f=d.getElementById(id);if(!f)return;
 f.addEventListener('submit',function(e){e.preventDefault();var err=$('.err',f),v={};
  keys.forEach(function(k){v[k]=(f.elements[k].value||'').trim()});
  var bad=!v.name||(v.phone!==undefined&&!/^[\d\s+()-]{10,}$/.test(v.phone))||(id==='msgf'&&(!v.contact||!v.msg));
  if(bad){err.classList.remove('ok');err.textContent='Please complete the required fields (name and a valid contact).';return}
  var body=keys.map(function(k){return labels[k]+': '+(v[k]||'-')}).join('\n');
  location.href='mailto:mariejaca@yahoo.com?subject='+encodeURIComponent(subject+' - '+v.name)+'&body='+encodeURIComponent(body);
  err.classList.add('ok');err.textContent='Your email app should open with your message ready to send.'})};

/* ---- WebGL flowing-light shader (hero + page heroes) ---- */
$$('canvas.fx').forEach(function(cv){
 var gl=cv.getContext('webgl',{antialias:false,alpha:false,powerPreference:'low-power'});if(!gl)return;
 var vs='attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}',
 fs='precision mediump float;uniform vec2 r;uniform float t;uniform vec2 m;'+
 'float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}'+
 'float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}'+
 'float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<5;i++){v+=a*n(p);p=p*2.02+vec2(3.1,1.7);a*=.5;}return v;}'+
 'void main(){vec2 uv=gl_FragCoord.xy/r;vec2 p=uv*vec2(r.x/r.y,1.)*2.4;'+
 'vec2 q=vec2(fbm(p+t*.05),fbm(p+vec2(5.2,1.3)-t*.04));'+
 'vec2 w=vec2(fbm(p+3.*q+vec2(1.7,9.2)+t*.08),fbm(p+3.*q+vec2(8.3,2.8)-t*.06));'+
 'float f=fbm(p+3.*w);'+
 'vec3 c=mix(vec3(.047,.027,.035),vec3(.88,.14,.44),smoothstep(.3,.9,f)*.9);'+
 'c=mix(c,vec3(.85,.69,.42),smoothstep(.66,.98,fbm(p*1.3+w*2.))*.6);'+
 'c+=vec3(.9,.25,.55)*.14*smoothstep(.5,0.,distance(uv,m));'+
 'c*=.55+.45*smoothstep(1.3,.2,distance(uv,vec2(.72,.45)));'+
 'gl_FragColor=vec4(c,1.);}';
 function sh(t,s){var o=gl.createShader(t);gl.shaderSource(o,s);gl.compileShader(o);return o}
 var pr=gl.createProgram();gl.attachShader(pr,sh(gl.VERTEX_SHADER,vs));gl.attachShader(pr,sh(gl.FRAGMENT_SHADER,fs));gl.linkProgram(pr);
 if(!gl.getProgramParameter(pr,gl.LINK_STATUS))return;gl.useProgram(pr);
 var b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),gl.STATIC_DRAW);
 var loc=gl.getAttribLocation(pr,'p');gl.enableVertexAttribArray(loc);gl.vertexAttribPointer(loc,2,gl.FLOAT,false,0,0);
 var ur=gl.getUniformLocation(pr,'r'),ut=gl.getUniformLocation(pr,'t'),um=gl.getUniformLocation(pr,'m'),S=.5,mx=.7,my=.5,tx=.7,ty=.5,vis=true,t0=performance.now();
 function size(){var w=cv.clientWidth,h=cv.clientHeight;cv.width=Math.max(2,w*S|0);cv.height=Math.max(2,h*S|0);gl.viewport(0,0,cv.width,cv.height)}
 size();addEventListener('resize',size);
 cv.parentNode.addEventListener('mousemove',function(e){var r=cv.getBoundingClientRect();tx=(e.clientX-r.left)/r.width;ty=1-(e.clientY-r.top)/r.height});
 new IntersectionObserver(function(e){vis=e[0].isIntersecting;if(vis&&!RM)frame()}).observe(cv);
 function frame(now){if(!vis)return;mx+=(tx-mx)*.04;my+=(ty-my)*.04;gl.uniform2f(ur,cv.width,cv.height);gl.uniform1f(ut,((now||performance.now())-t0)/1000+8);gl.uniform2f(um,mx,my);gl.drawArrays(gl.TRIANGLES,0,3);if(!RM)requestAnimationFrame(frame)}
 frame();cv.classList.add('live');
});
})();
