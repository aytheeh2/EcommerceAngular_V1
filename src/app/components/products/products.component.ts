import { Component } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, Router } from '@angular/router';
import { APIcallerService } from 'src/app/services/apicaller.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent {
  constructor(
    public api: APIcallerService,
    public router: Router,
    public active_route: ActivatedRoute,
  ) { }

  data: any;
  category = {
    "name": "",
    "image": ""
  }
  id: any;
  ngOnInit() {
    this.id = this.active_route.snapshot.paramMap.get('id');

    this.api.get_category_by_id(this.id).subscribe(response => {
      this.category = response;
      console.log(this.category, 'api all_categories');

    });
    this.api.get_products_in_category_by_id(this.id).subscribe(response => {
      console.log("get_products_in_category_by_id", response);
      this.data = response;
    })

  }

  detail(id: any) {
    this.api.get_product_details_by_id(id).subscribe(response => {
      console.log('detail(id)', response);
      this.router.navigate(['detail', id])
    })
  }

  add_to_cart(id: any) {
    this.router.navigate(['cart',id])
  }
}
