import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from '../../environments/environment';
import { Person } from '../models/person.model';

@Injectable({ providedIn: 'root' })
export class PersonsService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getPersons(): Observable<Person[]> {
    return this.http.get<{ success: boolean; data: Person[] }>(
      `${this.apiUrl}/persons`
    ).pipe(map(res => res.data));
  }
}