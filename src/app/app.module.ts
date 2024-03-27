import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

//
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

import { CategoryComponent } from './components/category/category.component';
import { ProductsComponent } from './components/products/products.component';
import { DetailComponent } from './components/detail/detail.component';
import { RegisterComponent } from './components/register/register.component';
import { LoginComponent } from './components/login/login.component';
import { CartComponent } from './components/cart/cart.component';
import { OrderComponent } from './components/order/order.component';

@NgModule({
  declarations: [
    AppComponent,
    CategoryComponent,
    ProductsComponent,
    DetailComponent,
    RegisterComponent,
    LoginComponent,
    CartComponent,
    OrderComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    RouterModule,


  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
