const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'}).catch(async()=>await chromium.launch());
const p=await b.newPage({viewport:{width:1200,height:900}});
await p.setContent('<html><body style="margin:0">'+require('fs').readFileSync('z.svg','utf8')+'</body></html>');
await p.waitForTimeout(500);await p.screenshot({path:'z.png'});await b.close();})();
