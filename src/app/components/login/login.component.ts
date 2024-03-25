import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIcallerService } from 'src/app/services/apicaller.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(
    public api: APIcallerService,
    public router: Router,
  ) { }
  data = {
    'username': '',
    'password': ''
  };



  onSubmit() {
    console.log(this.data);
    this.api.login_by_token(this.data).subscribe(response => {
      console.log('login_by_token', response);
      localStorage.setItem('token', 'Token ' + response.token);
      console.log(localStorage.getItem('token'));
      this.router.navigate(['']);

    })

  };

}
