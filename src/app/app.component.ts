import { Component } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  serverName='Apollo';
  serverID=11;
  serverStatus='Offline';
  statusFlag=false;
  buttonState=false;
  
  toggleServerStatus(){
    this.statusFlag=!this.statusFlag;
    if(this.statusFlag)
    {
      this.serverStatus = 'Running';
    }
    else
    {
      this.serverStatus = 'Offline';
    }
  }
}
