const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const c=await b.newContext({locale:'en-US'});const p=await c.newPage({viewport:{width:800,height:900}});
await p.setContent('<html><body style="font-family:Arial;max-width:760px;margin:auto">'+require('fs').readFileSync('tool.html','utf8')+'</body></html>');
await p.screenshot({path:'a.png',fullPage:true});
await p.click('[data-m="bed"]');await p.locator('.res').screenshot({path:'b.png'});
await p.click('[data-m="dining"]');await p.locator('.res').screenshot({path:'c.png'});
await p.setViewportSize({width:380,height:900});await p.click('[data-m="living"]');await p.screenshot({path:'m.png',fullPage:true});
await b.close();})();
