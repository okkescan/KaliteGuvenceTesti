import http from 'k6/http';
import { sleep } from 'k6';
export const options = {
  vus: 100, //Kullanıcı sayısı
  duration: '30s', //Test süresi
};
export default function () {
  http.get('http://okkess.online'); //Http isteğinin gönderileceği web adresimiz
  sleep(1);
}
