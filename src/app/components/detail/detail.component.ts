import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { APIcallerService } from 'src/app/services/apicaller.service';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent {

  constructor(
    public api: APIcallerService,
    public router: Router,
    public active_route: ActivatedRoute,
  ) { }
  product_detail: any;
  id: any;
  ngOnInit() {
    this.id = this.active_route.snapshot.paramMap.get('id');
    this.api.get_product_details_by_id(this.id).subscribe(response => {
      console.log('get_product_by_id', response);
      this.product_detail = response;
    })
  }
}
