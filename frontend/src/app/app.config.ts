import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { Routes } from '@angular/router';
import { PersonsListComponent } from './components/persons-list/persons-list.component';

const routes: Routes = [
  { path: '', component: PersonsListComponent },
  { path: '**', redirectTo: '' }
];

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(withFetch())
  ]
};