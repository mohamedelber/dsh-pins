const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const p=await b.newPage({viewport:{width:420,height:1500}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body style="margin:0;font-family:sans-serif">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
const out=async(n,all)=>{const t=await p.evaluate((all)=>[...document.querySelectorAll(all?'#vv,.kpi,#tp li':'#vv,.kpi')].map(e=>e.innerText.replace(/\n/g,' | ')).join(' || '),all);console.log('\n#',n,':',t)};
await out('default',1);
for(const w of ['96','144','192']){await p.click(`[data-w="${w}"]`);for(const t of ['tall','wain','full','grid']){await p.click(`[data-t="${t}"]`);await out(w+' '+t)}}
await p.click('[data-w="120"]');await p.click('[data-t="grid"]');await p.screenshot({path:'a.png',fullPage:true});
await p.click('summary');await p.selectOption('#bd','4');await p.fill('#ww','123.5');await p.click('[data-t="tall"]');await out('AMM 123.5 1x4',1);
await p.fill('#wh','120');await p.click('[data-t="full"]');await out('10ft ceiling full');
await p.selectOption('#un','cm');await out('cm',1);
await p.screenshot({path:'m.png',fullPage:true});
console.log('errors',errs);await b.close()})();
