import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class APIcallerService {

  constructor(
    public http: HttpClient,
  ) { }
  //home page
  _base_url = `http://127.0.0.1:8000/`;
  all_categories = `shop/cat/`;

  get_categories() {
    return this.http.get<any>(`http://127.0.0.1:8000/shop/cat`);
  };

  get_category_by_id(id: any) {
    return this.http.get<any>(`http://127.0.0.1:8000/shop/cat/${id}/`);
  }

  get_products_in_category_by_id(id: any) {
    return this.http.get<any>(`http://127.0.0.1:8000/allproducts/${id}/`);
  };

  get_product_details_by_id(id: any) {
    return this.http.get<any>(`http://127.0.0.1:8000/detail/${id}/`)
  }

  register(data: any) {
    return this.http.post(`http://127.0.0.1:8000/shop/user/`, data)
  }

  login_by_token(data: any) {
    return this.http.post<any>(`http://127.0.0.1:8000/api-token-auth/`, data)
  }

  token: any;
  headers: any;

  logout_by_token() {
    this.token = localStorage.getItem('token');
    this.headers = new HttpHeaders({
      "Authorization": this.token,
    });

    return this.http.get<any>(`http://127.0.0.1:8000/logout/`, { 'headers': this.headers });
  }

  add_to_cart_by_id(id: any) {
    this.token = localStorage.getItem('token');
    console.log(this.token);

    this.headers = new HttpHeaders({
      "Authorization": this.token
    })

    console.log('headers:',this.headers);

    return this.http.get(`http://127.0.0.1:8000/cart/addtocart/${id}/`, { headers: this.headers })
  }


}
