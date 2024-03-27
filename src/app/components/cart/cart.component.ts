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

  cart_total: any;

  ngOnInit() {
    this.productId = this.route.snapshot.paramMap.get('id');
    if (this.productId) {
      this.api.add_to_cart_by_id(this.productId).subscribe(res => {
        console.log('ngOnInit of CartComponent', res);
        console.log('added to cart');
        this.cart_objects = res;
        localStorage.setItem('cart_objects', this.cart_objects)

        this.cart_total = 0;
        for (var i in this.cart_objects) {
          // console.log('i', this.cart_objects[i]['subtotal']);
          this.cart_total += this.cart_objects[i]['subtotal']
        }
        console.log('cart_total', this.cart_total);

      });
    }
  }

  detail(id: any) {
    this.api.get_product_details_by_id(id).subscribe(response => {
      console.log('detail(id)', response);
      this.router.navigate(['detail', id])
    })
  }

  add(id: any) {
    this.api.add_to_cart_by_id(id).subscribe(res => {
      console.log('add_to_cart_by_id', res);
      this.cart_objects = res;
      // this.ngOnInit();
      this.cart_total = 0;
      for (var i in this.cart_objects) {
        // console.log('i', this.cart_objects[i]['subtotal']);
        this.cart_total += this.cart_objects[i]['subtotal']
      }
      console.log('cart_total', this.cart_total);
    })
  }

  sub(id: any) {
    console.log(id);

    this.api.sub_from_cart(id).subscribe(res => {
      console.log('sub_from_cart', res);
      this.cart_objects = res;
      this.cart_total = 0;
      for (var i in this.cart_objects) {
        // console.log('i', this.cart_objects[i]['subtotal']);
        this.cart_total += this.cart_objects[i]['subtotal']
      }
      console.log('cart_total', this.cart_total);
    });
  }

  cart_remove(id: any) {
    this.api.remove_item_from_cart_by_id(id).subscribe(res => {
      console.log('remove_item_from_cart_by_id', res);
      this.cart_objects = res;
      this.cart_total = 0;
      for (var i in this.cart_objects) {
        // console.log('i', this.cart_objects[i]['subtotal']);
        this.cart_total += this.cart_objects[i]['subtotal']
      }
      console.log('cart_total', this.cart_total);
    });
  }


}
