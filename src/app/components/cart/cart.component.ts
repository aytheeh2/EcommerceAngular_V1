import { Component, QueryList } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { APIcallerService } from 'src/app/services/apicaller.service';
@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent {

  constructor(
    private api: APIcallerService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  productId: any;

  cart_objects: any;

  ngOnInit() {
    this.productId = this.route.snapshot.paramMap.get('id');
    this.api.add_to_cart_by_id(this.productId).subscribe(res => {
      console.log('ngOnInit of CartComponent', res);
      console.log('added to cart');
      this.cart_objects = res;
      localStorage.setItem('cart_objects', this.cart_objects)
    })
  }


}
