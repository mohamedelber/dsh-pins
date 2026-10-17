const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const loc of ['en-US','en-GB']){const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:820,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:780px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const T=async(l)=>console.log(loc,l,'|',await p.textContent('#vd'),'|',await p.textContent('#k1'),'|',await p.textContent('#k2'),'|',(await p.innerText('#by')).replace(/\n+/g,' / ').slice(0,300),'|',await p.textContent('#wn'));
await T('living default');
await p.fill('#rl',loc==='en-US'?'12':'366');await p.fill('#rw',loc==='en-US'?'10':'305');await T('living small room');
await p.click('[data-m="dining"]');await T('dining');await p.click('[data-t="round"]');await T('dining round');
await p.click('[data-m="bed"]');await T('bed');await p.selectOption('#bp','full');await T('bed full');
await p.click('[data-m="hall"]');await T('hall');
await p.click('[data-m="living"]');await T('back living');
await p.click('[data-u="cm"]');await T('to cm');
if(loc==='en-US'){await p.screenshot({path:'s1.png',fullPage:true});}
console.log('errors',errs);}
await b.close();})();
