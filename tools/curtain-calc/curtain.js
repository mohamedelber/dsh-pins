(function(){
var R=document.getElementById('dsh-curtain');if(!R)return;
var IN=2.54,unit='cm',reg='uk',mount='out',len='floor';
try{var lg=(navigator.language||'').toLowerCase();if(lg.indexOf('en-us')===0){unit='in';reg='us'}}catch(e){}
function $(i){return document.getElementById(i)}
function g(i){var v=parseFloat($(i).value);if(isNaN(v)||v<0)v=0;return unit==='in'?v*IN:v}
function s(i,cm){$(i).value=unit==='in'?Math.round(cm/IN*2)/2:Math.round(cm)}
function f(cm){return unit==='in'?(Math.round(cm/IN*2)/2)+' in':Math.round(cm)+' cm'}
function both(cm){return Math.round(cm)+' cm ('+Math.round(cm/IN)+' in)'}
var UKW=[[46,117],[66,168],[90,228],[112,284]],UKD=[[54,137],[72,183],[90,229],[108,274]];
var UKP=[120,150,180,210,240,300];
var USL=[63,84,96,108,120],USR=[[28,48],[48,84],[66,120],[120,170]];
var ids=['ww','wh','wc','sf','ex'];
function calc(){
var ww=g('ww'),wh=g('wh'),wc=g('wc'),sf=g('sf'),ex=g('ex');
var fu=parseFloat($('fu').value)||2,np=parseInt($('np').value)||2;
var warn=[],tips=[];
var poleLen,above,poleTop;
if(mount==='in'){poleLen=Math.max(0,ww-1);above=0;}
else{poleLen=ww+2*ex;
 var ph=$('ph').value;
 if(ph==='half')above=wc/2;else if(ph==='top')above=Math.max(0,wc-5);else above=Math.min(15,Math.max(0,wc-5));
}
poleTop=sf+wh+above;
var drop;
if(len==='sill'){drop=above+wh-1}
else if(len==='apron'){drop=above+wh+15}
else if(len==='floor'){drop=poleTop-1}
else{drop=poleTop+5}
var total=poleLen*fu,each=total/np;
if(mount==='out'?(above+3>wc?wc>0:false):false)warn.push('There is very little space above the frame. Consider a ceiling-fixed track, or fit the pole just under the ceiling.');
if(len==='apron'?(sf<20?sf>0:false):false)warn.push('The sill is close to the floor, so below-sill curtains would almost reach it. Choose floor length instead.');
if(mount==='in'?(len==='floor'||len==='puddle'):false)tips.push('Inside a recess, floor-length curtains only work if nothing blocks the recess below the window.');
$('wn').innerHTML=warn.map(function(x){return '<div class="warn">'+x+'</div>'}).join('');
$('k1').textContent=f(poleLen);$('k1e').textContent=mount==='in'?'Fits inside the recess':'Window + '+f(ex)+' each side, without finials';
$('k2').textContent=f(drop);$('k2e').textContent=mount==='in'?'From the top of the track':'From the top of the pole (eyelets) or the ring eye';
$('k3').textContent=f(each);$('k3e').textContent=np===2?'Flat width of each curtain, '+fu+'x fullness':'Flat width, '+fu+'x fullness';
$('k4').textContent=f(poleTop);$('k4e').textContent=mount==='in'?'Top of the recess':f(above)+' above the frame';
var by='';
if(reg==='uk'){
 var need=np===2?each:each/2;var w=null;for(var i=0;i<UKW.length;i++){if(UKW[i][1]>=need-2){w=UKW[i];break}}
 var d=null,d0=null;for(var j=0;j<UKD.length;j++){if(UKD[j][1]>=drop-1){d=UKD[j];break}d0=UKD[j]}
 var canLower=(mount==='out'?(d0?(drop-d0[1])<=above-3:false):false);
 if(w?(d||d0):false){
  var use=d,lower=0;
  if(canLower?(!d||d[1]-drop>drop-d0[1]):false){use=d0;lower=drop-1-d0[1]+1}
  by+='<p><strong>Ready-made pair: '+w[0]+' x '+use[0]+' in</strong> ('+w[1]+' x '+use[1]+' cm), width x drop of each curtain.</p>';
  if(use===d0){by+='<p>Fit the pole '+Math.round(drop-d0[1])+' cm lower ('+Math.round(above-(drop-d0[1]))+' cm above the frame) so this drop ends '+endTxt()+'.</p>'}
  else{var extra=d[1]-drop;
   if(extra>4)by+='<p>That drop is '+Math.round(extra)+' cm longer than you need. Hem the curtains, use a tape-adjustable heading, or '+((mount==='out'?(len!=='sill'?above+extra<=wc-3:false):false)?'raise the pole by '+Math.round(extra)+' cm.':'choose made-to-measure.')+'</p>';}
  if(np===1)by+='<p>Ready-made curtains come in pairs. For one curtain, buy a pair and use one, or order a single made-to-measure curtain about '+both(each)+' wide.</p>';
 }else{
  by+='<p><strong>Made-to-measure</strong> is the best fit: about '+both(each)+' wide per curtain and '+both(drop)+' long.</p>';
  if(!w)by+='<p>Your window is wider than the largest ready-made pair. You can also hang two pairs side by side.</p>';
  if(!(d||d0))by+='<p>Your drop is outside standard ready-made sizes.</p>';
 }
 var pl=null;for(var k=0;k<UKP.length;k++){if(UKP[k]>=poleLen){pl=UKP[k];break}}
 by+='<p>'+(mount==='in'?'Track: ':'Pole: ')+(pl?'a '+pl+' cm '+(mount==='in'?'track cut to size':'pole')+' (or an extendable one that covers '+Math.round(poleLen)+' cm)':'longer than standard poles, so use a corded track or a jointed pole')+'.</p>';
}else{
 var ein=each/IN,tin=total/IN,dIn=drop/IN,pIn=poleLen/IN;
 var panels=Math.max(np,Math.ceil(tin/52));if(np===2?panels%2:false)panels++;
 by+='<p><strong>'+panels+' panels about 50 to 54 in wide</strong> give a total width of about '+Math.round(panels*52)+' in, enough for '+fu+'x fullness on a '+Math.round(pIn)+' in rod.</p>';
 if(panels>np){var fx=Math.round(np*52/pIn*10)/10;by+='<p>On a budget, '+np+' panel'+(np>1?'s':'')+' give about '+fx+'x fullness, a flatter look.</p>'}
 var L=null,L0=null;for(var a=0;a<USL.length;a++){if(USL[a]>=dIn-0.5){L=USL[a];break}L0=USL[a]}
 var abIn=above/IN,useL=L;
 if(mount==='out'?(L0?((dIn-L0)<=abIn-1?(!L||L-dIn>dIn-L0):false):false):false)useL=L0;
 if(useL){by+='<p><strong>Panel length: '+useL+' in</strong> (you need '+(Math.round(dIn*2)/2)+' in).</p>';
  if(useL===L0?useL!==L:false){by+='<p>Mount the rod '+(Math.round((dIn-L0)*2)/2)+' in lower ('+(Math.round((abIn-(dIn-L0))*2)/2)+' in above the frame) so these panels end '+endTxt()+'.</p>'}
  else{var ex2=L-dIn;
  if(ex2>1.5)by+='<p>That is '+(Math.round(ex2*2)/2)+' in longer than you need. Hem them, or '+((mount==='out'?(len!=='sill'?abIn+ex2<=wc/IN-1:false):false)?'raise the rod by '+(Math.round(ex2*2)/2)+' in.':'choose custom-length panels.')+'</p>';}
 }else by+='<p>Your drop is longer than standard panels (up to 120 in), so choose custom-length curtains.</p>';
 var rr=null;for(var b=0;b<USR.length;b++){if(pIn>=USR[b][0]?pIn<=USR[b][1]:false){rr=USR[b];break}}
 by+='<p>Rod: '+(rr?'an adjustable rod that extends from '+rr[0]+' to '+rr[1]+' in':'a custom or extra-long rod with a center support')+'.</p>';
}
$('by').innerHTML=by;
var vd=$('vd');
vd.textContent=(np===2?'You need a pair of curtains about ':'You need one curtain about ')+f(each)+' wide and '+f(drop)+' long, on a '+f(poleLen)+' '+(mount==='in'?'track':'pole')+'.';
if(len==='sill'||len==='apron')tips.push('Short curtains are best above a radiator so heat can rise into the room.');
if(len==='floor'||len==='puddle')tips.push('Floor-length curtains make a ceiling look higher, especially with the pole fitted well above the frame.');
if(mount==='out')tips.push('Measure the pole without its finials, and leave room for the end brackets.');
tips.push('Measure in two or three places and use the largest figure; walls and floors are rarely perfectly straight.');
$('tp').innerHTML=tips.map(function(x){return '<li>'+x+'</li>'}).join('');
draw(ww,wh,wc,sf,poleLen,above,drop);
summary={t:vd.textContent,p:f(poleLen),d:f(drop),e:f(each),h:f(poleTop)};
}
var summary={};
function endTxt(){return {sill:'just above the sill',apron:'below the sill',floor:'just above the floor',puddle:'on the floor'}[len]}
function draw(ww,wh,wc,sf,pl,above,drop){
var H=sf+wh+wc,Wd=Math.max(pl,ww)+60;if(H<=0||Wd<=0)return;
var VW=300,VH=Math.max(180,Math.min(360,VW*H/Wd)),sc=Math.min((VW-20)/Wd,(VH-20)/H);
var cx=VW/2,fl=VH-10,y=function(cm){return fl-cm*sc};
var wx=cx-ww*sc/2,wy=y(sf+wh),wH=wh*sc,ptop=y(sf+wh+above),half=pl*sc/2;
var o='<svg viewBox="0 0 '+VW+' '+VH+'" xmlns="http://www.w3.org/2000/svg">';
o+='<rect x="0" y="0" width="'+VW+'" height="'+VH+'" fill="#FBF6EF"/>';
o+='<line x1="0" y1="'+y(H)+'" x2="'+VW+'" y2="'+y(H)+'" stroke="#B9AD9F" stroke-width="2"/>';
o+='<line x1="0" y1="'+fl+'" x2="'+VW+'" y2="'+fl+'" stroke="#342E2A" stroke-width="3"/>';
o+='<rect x="'+wx+'" y="'+wy+'" width="'+ww*sc+'" height="'+wH+'" fill="#DCEAF0" stroke="#fff" stroke-width="5"/>';
o+='<line x1="'+cx+'" y1="'+wy+'" x2="'+cx+'" y2="'+(wy+wH)+'" stroke="#fff" stroke-width="3"/>';
o+='<rect x="'+(wx-6)+'" y="'+(wy+wH)+'" width="'+(ww*sc+12)+'" height="5" fill="#EFE6DA" stroke="#D8CBBB"/>';
var cw=Math.max(14,Math.min(half*0.55,ww*sc*0.35)),cb=ptop+drop*sc;
[cx-half,cx+half-cw].forEach(function(x0){o+='<rect x="'+x0+'" y="'+(ptop+2)+'" width="'+cw+'" height="'+Math.max(4,cb-ptop-2)+'" fill="#A9BCA3" opacity=".92"/>';for(var q=1;q<4;q++){o+='<line x1="'+(x0+cw*q/4)+'" y1="'+(ptop+4)+'" x2="'+(x0+cw*q/4)+'" y2="'+(cb-2)+'" stroke="#8FA689" stroke-width="1"/>'}});
o+='<line x1="'+(cx-half-6)+'" y1="'+ptop+'" x2="'+(cx+half+6)+'" y2="'+ptop+'" stroke="#342E2A" stroke-width="3"/>';
o+='<circle cx="'+(cx-half-7)+'" cy="'+ptop+'" r="3.5" fill="#342E2A"/><circle cx="'+(cx+half+7)+'" cy="'+ptop+'" r="3.5" fill="#342E2A"/>';
o+='<text x="'+cx+'" y="'+(ptop-6)+'" font-size="11" text-anchor="middle" fill="#C85A32" font-weight="700">'+f(pl)+'</text>';
o+='<text x="'+(cx+half+12)+'" y="'+((ptop+cb)/2)+'" font-size="11" fill="#C85A32" font-weight="700">'+f(drop)+'</text>';
o+='</svg>';
$('vz').innerHTML=o;
}
function setReg(r){reg=r;R.querySelectorAll('[data-r]').forEach(function(x){x.classList.toggle('on',x.getAttribute('data-r')===r)})}
function setUnit(u,convert){var vals=ids.map(function(i){return g(i)});unit=u;if(convert)ids.forEach(function(i,k){s(i,vals[k])});R.querySelectorAll('[data-u]').forEach(function(x){x.classList.toggle('on',x.getAttribute('data-u')===u)})}
R.querySelectorAll('[data-r]').forEach(function(b){b.addEventListener('click',function(){setReg(b.getAttribute('data-r'));calc()})});
R.querySelectorAll('[data-u]').forEach(function(b){b.addEventListener('click',function(){var u=b.getAttribute('data-u');if(u!==unit){setUnit(u,true);calc()}})});
R.querySelectorAll('[data-m]').forEach(function(b){b.addEventListener('click',function(){mount=b.getAttribute('data-m');R.querySelectorAll('[data-m]').forEach(function(x){x.classList.toggle('on',x===b)});$('outset').style.display=mount==='in'?'none':'';calc()})});
R.querySelectorAll('[data-l]').forEach(function(b){b.addEventListener('click',function(){len=b.getAttribute('data-l');R.querySelectorAll('[data-l]').forEach(function(x){x.classList.toggle('on',x===b)});calc()})});
ids.forEach(function(i){$(i).addEventListener('input',calc)});['ph','fu','np'].forEach(function(i){$(i).addEventListener('change',calc)});
$('cp').addEventListener('click',function(){var t='My curtain measurements (dailyspacehacks.com)\n'+summary.t+'\nPole/track length: '+summary.p+'\nCurtain drop: '+summary.d+'\nWidth of each curtain: '+summary.e+'\nPole height from floor: '+summary.h;var b=$('cp');function ok(){b.textContent='Copied!';setTimeout(function(){b.textContent='Copy my measurements'},1800)}try{navigator.clipboard.writeText(t).then(ok,function(){window.prompt('Copy your measurements:',t)})}catch(e){window.prompt('Copy your measurements:',t)}});
$('pr').addEventListener('click',function(){window.print()});
var u0=unit;unit='cm';s('ww',120);s('wh',130);s('wc',40);s('sf',90);s('ex',20);
setUnit(u0,true);setReg(reg);calc();
})();
