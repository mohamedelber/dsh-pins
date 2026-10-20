const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const p=await b.newPage({viewport:{width:420,height:1500}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="margin:0;font-family:sans-serif">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const out=async(n)=>{const t=await p.evaluate(()=>[...document.querySelectorAll('#vv,.kpi,#tp li')].map(e=>e.innerText.replace(/\n/g,' | ')).join(' || '));console.log('\n#',n,':',t)};
await out('default');
for(const r of ['kit','bed','bath','din','off','hall']){await p.click(`[data-r="${r}"]`);for(const s of ['0','3']){await p.click(`[data-s="${s}"]`);const t=await p.evaluate(()=>[...document.querySelectorAll('#vv,.kpi')].map(e=>e.innerText.replace(/\n/g,' | ')).join(' || '));console.log(r,s,':',t)}}
await p.click('[data-r="liv"]');await p.click('[data-s="1"]');await p.screenshot({path:'a.png',fullPage:true});
await p.click('summary');await p.selectOption('#ch','12');await out('liv 12ft');
await p.selectOption('#ch','8');await p.selectOption('#un','m');await p.fill('#rl','5');await p.fill('#rw','4');await out('5x4 m');
await p.selectOption('#ls','4');await p.click('[data-r="kit"]');await out('kit 4in metric');
await p.screenshot({path:'m.png',fullPage:true});
console.log('errors',errs);await b.close()})();
