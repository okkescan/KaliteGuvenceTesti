import http from 'k6/http'
import {sleep} from 'k6'

export let options = {
stages:[
    {duration:'10s',target:50},
    {duration:'15s',target:70},
    {duration:'1m',target:90},
    {duration:'2m',target:100}
],

};
const weburl = "http://okkess.online";
export default () =>{
   
    
    http.batch([
        
        ['GET','http://okkess.online/Anasayfa.aspx'],
        ['GET','http://okkess.online/BlogIcerik.aspx?ID=1'],
        ['GET','http://okkess.online/KategoriDetay.aspx?KATEGORIID=%204'],
        ['GET','http://okkess.online/Hakkimda.aspx']
    ]);
    sleep(1)
}