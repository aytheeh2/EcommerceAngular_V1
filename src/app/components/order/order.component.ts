import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { APIcallerService } from 'src/app/services/apicaller.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent {
  constructor(
    private api: APIcallerService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  data: any = {
    address: "",
    phone: "",
    acctnum: ""
  }


  onSubmit() {
    console.log(this.data);
    this.api.orderform(this.data).subscribe(res => {
      console.log('orderform', res);

    });


  }

}
