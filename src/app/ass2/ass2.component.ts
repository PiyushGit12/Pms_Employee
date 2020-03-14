import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-ass2',
  templateUrl: './ass2.component.html',
  styleUrls: ['./ass2.component.css']
})
export class Ass2Component implements OnInit {

  name='saurabh';
 disableButtonFlag=false;
flag=true;
toggleFlag()
{
  this.flag=!this.flag;
}

  constructor() { }

  ngOnInit() {
  }

buttonFlagStats()
{
  if(this.name.length==0)
{
  return true;
}
return false;
}

  resetNameButton()
  {
    this.name="";
    this.buttonFlagStats();
    
  }
}
