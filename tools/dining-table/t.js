const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for (const loc of ['en-US','en-GB']){
const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:800,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const r=async()=>p.evaluate(()=>['vv','kt','km','kr'].map(i=>document.getElementById(i).textContent).join(' | '));
console.log(loc,'default:',await r());
for(const n of ['2','4','8','12']){await p.click('[data-n="'+n+'"]');console.log(n,await r())}
await p.click('[data-s="round"]');console.log('round12',await r());
await p.click('[data-n="4"]');console.log('round4',await r());
await p.click('[data-s="square"]');await p.click('[data-n="6"]');console.log('sq6',await r(),await p.evaluate(()=>document.getElementById('tp').textContent.slice(0,120)));
await p.click('[data-s="rect"]');await p.click('summary');
await p.fill('#rl',loc==='en-US'?'144':'360');await p.fill('#rw',loc==='en-US'?'120':'300');console.log('room',await r());
await p.fill('#rw',loc==='en-US'?'100':'250');console.log('small',await r());
await p.fill('#rw',loc==='en-US'?'80':'200');console.log('tiny',await r());
await p.selectOption('#cs','1');await p.fill('#rw',loc==='en-US'?'130':'330');console.log('wide',await r());
await p.click('[data-u="'+(loc==='en-US'?'cm':'in')+'"]');console.log('switch',await r(),await p.inputValue('#rw'));
if(loc==='en-US'){await p.screenshot({path:'a.png',fullPage:true});await p.setViewportSize({width:380,height:900});await p.screenshot({path:'m.png',fullPage:true});}
console.log('errors',errs);await c.close();}
await b.close();})();
