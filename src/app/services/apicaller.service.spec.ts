import { TestBed } from '@angular/core/testing';

import { APIcallerService } from './apicaller.service';

describe('APIcallerService', () => {
  let service: APIcallerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(APIcallerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
