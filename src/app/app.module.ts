import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms';

import { AppComponent } from './app.component';
import { ServerComponent } from './servers/server.component';
import { Ass2Component } from './ass2/ass2.component';


@NgModule({
  declarations: [
    AppComponent,
    ServerComponent,
    Ass2Component
  ],
  imports: [
    BrowserModule,FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
