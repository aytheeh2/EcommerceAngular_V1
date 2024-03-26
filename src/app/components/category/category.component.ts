import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIcallerService } from 'src/app/services/apicaller.service';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent {
  constructor(
    public api: APIcallerService,
    public router: Router,
  ) { }

  data: any;
  ngOnInit() {
    this.api.get_categories().subscribe(response => {
      this.data = response;
      console.log(this.data, 'api all_categories');

    });
  }

  go_to_category_by_id(id: any) {
    console.log('category id:', id);
    this.router.navigate(['product', id])
  }
}

