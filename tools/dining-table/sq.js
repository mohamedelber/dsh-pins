const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:800,height:900}});
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
await p.click('[data-s="square"]');await p.click('[data-n="8"]');const el=p.locator('#vz');await el.screenshot({path:'sq8.png'});
await p.click('[data-s="rect"]');await p.click('[data-n="10"]');await el.screenshot({path:'r10.png'});await b.close()})();
