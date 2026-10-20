const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const p=await b.newPage({viewport:{width:420,height:1400}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="margin:0;font-family:sans-serif">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const out=async(n)=>{const t=await p.evaluate(()=>[...document.querySelectorAll('#vv,.kpi')].map(e=>e.innerText.replace(/\n/g,' | ')).join(' || '));console.log(n,':',t)};
for(const h of ['60','68','76']){await p.click(`[data-h="${h}"]`);await p.click('[data-m="sit"]');await out(h+' sit');await p.click('[data-m="stand"]');await out(h+' stand')}
await p.screenshot({path:'a.png',fullPage:true});
await p.click('summary');await p.selectOption('#un','cm');await p.fill('#hh','165');await out('165cm stand');await p.click('[data-m="sit"]');await out('165cm sit');await p.fill('#eh','66');await out('elbow 66cm');
await p.screenshot({path:'m.png',fullPage:true});
console.log('errors',errs);await b.close()})();
