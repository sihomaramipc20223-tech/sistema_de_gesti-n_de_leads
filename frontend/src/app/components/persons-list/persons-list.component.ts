import { Component, OnInit } from '@angular/core';
import { PersonsService } from '../../services/persons.service';
import { Person } from '../../models/person.model';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-persons-list',
  standalone: true,
  imports: [CommonModule], 
  templateUrl: './persons-list.component.html',
  styleUrls: ['./persons-list.component.scss']
})
export class PersonsListComponent implements OnInit {
  persons: Person[] = [];
  loading = true;
  error = '';

  constructor(private personsService: PersonsService) {}

  ngOnInit(): void {
    this.loadPersons();
  }

  loadPersons(): void {
    this.loading = true;
    this.personsService.getPersons().subscribe({
      next: (data) => {
        this.persons = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Error al cargar personas';
        this.loading = false;
      }
    });
  }
}