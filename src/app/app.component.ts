import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIcallerService } from './services/apicaller.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(
    public api: APIcallerService,
    public router: Router
  ) { }
  title = 'AngularEcom';
  navbar_dropdowns: any;
  ngOnInit() {
    this.api.get_categories().subscribe(response => {
      console.log("navbar_dropdowns", response);
      this.navbar_dropdowns = response;
    })
  }

  logout() {
    if (confirm("logout?")) {
      this.api.logout_by_token().subscribe(response => {
        console.log('logout_by_token', response);
        localStorage.removeItem('token');
        console.log(localStorage);
      })
    }
  }



}
