import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { APIcallerService } from 'src/app/services/apicaller.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  constructor(
    public api: APIcallerService,
    public router: Router,
    public active_route: ActivatedRoute,
  ) { }


  data = {
    'username': '',
    'password': ''
  }

  onSubmit() {
    console.log(this.data);
    this.api.register(this.data).subscribe(response => {
      console.log('register', response);
      this.router.navigate(['']);
      this.data = {
        'username': '',
        'password': ''
      }
      
    })
  }

}
