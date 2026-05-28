import { Component } from '@angular/core';
import { PersonsListComponent } from './components/persons-list/persons-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [PersonsListComponent],   // ← esto es clave
  templateUrl: './app.html',
})
export class AppComponent {}