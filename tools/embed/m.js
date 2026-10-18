const {chromium}=require('playwright');const fs=require('fs');
const T=JSON.parse(fs.readFileSync('out/tools.json'));
const css=fs.readFileSync('emb.css','utf8');
(async()=>{const b=await chromium.launch();const H={};
for(const t of T){const es=t[2];const pg=fs.readFileSync('out/page-'+es+'.html','utf8').replace(/<!--.*?-->/g,'');
for(const loc of ['en-US','en-GB']){const c=await b.newContext({locale:loc});const p=await c.newPage({viewport:{width:760,height:600}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.setContent('<html><body class="dsh-embed" style="margin:0;font-family:Arial,sans-serif;font-size:16px">'+pg+'</body></html>');
const h=await p.evaluate(()=>document.documentElement.scrollHeight);H[es]=Math.max(H[es]||0,h);
if(errs.length)console.log(es,loc,errs);
if(es==='storage-unit-size-calculator'&&loc==='en-US')await p.screenshot({path:'p1.png',fullPage:true});
await c.close();}}
// button preview
const p=await b.newPage({viewport:{width:760,height:600}});
const btn=fs.readFileSync('out/btn-wallpaper-calculator.html','utf8');
await p.setContent('<html><head><style>'+css+'</style></head><body style="font-family:Arial;padding:20px">'+btn+btn+'</body></html>');
await p.locator('summary').nth(1).click();await p.screenshot({path:'b1.png',fullPage:true});
await p.locator('.ecp').nth(1).click();await p.waitForTimeout(300);console.log('btn',await p.locator('.ecp').nth(1).textContent());
await p.setViewportSize({width:375,height:600});await p.screenshot({path:'b2.png',fullPage:true});
for(const k in H)H[k]=Math.ceil((H[k]+24)/10)*10;
fs.writeFileSync('heights.json',JSON.stringify(H,null,1));console.log(H);await b.close();})();
