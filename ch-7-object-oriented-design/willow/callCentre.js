class CallCentre {
  constructor() {
    this.respondents = [];
    this.managers = [];
    this.directors = [];
  }

  hire(employee) {
    employee.workPlace = this;
    if (employee instanceof Respondent) {
      this.respondents.push(employee);
    }
    if (employee instanceof Manager) {
      this.managers.push(employee);
    }
    if (employee instanceof Director) {
      this.directors.push(employee);
    }
  }

  dispatchCall(call, level=1) {
    call.handler = null;
    let pool = level === 1 ? this.respondents : level === 2 ? this.managers : this.directors;
    for (const employee of pool) {
      if (employee.available) {
        employee.available = false;
        call.handler = employee;
        break
      }
    }
    if (!call.handler) {
      if (level == 2) {
        this.dispatchCall(call, level=3);
      } else {
        this.selfDestruct();
      }
    }
    call.handler.tryToHandle(call);
  }

  selfDestruct() {
    throw new Error('We have failed the customer.')
  }

  escalate(call) {
    if (call.handler instanceof Respondent) {
      this.dispatchCall(call, 2);
    } else if (call.handler instanceof Manager) {
      this.dispatchCall(call, 3);
    } else {
      this.selfDestruct();
    }
  }
}


class Employee {
  capability;
  empowerment;
  jobTitle;
  workPlace;

  constructor(capability) {
    this.capability = capability;
    this.available = true;
  }

  get effectiveness() {
    return this.capability + this.empowerment;
  }

  rejoice() {
    console.log(`${this.jobTitle} with effectiveness ${this.effectiveness} is rejoicing!`);
  }

  despair() {
    console.log(`${this.jobTitle} with effectiveness ${this.effectiveness} is despairing :(`);
  }

  tryToHandle(call) {
    if (call.difficulty <= this.effectiveness) {
      this.rejoice();
      this.available = true;
    } else {
      this.despair()
      this.available = true;
      this.workPlace.escalate(call);
    }
  }
}

class Respondent extends Employee {
  constructor(capability) {
    super(capability);
    this.empowerment = 1;
    this.jobTitle = 'Respondent'
  }
}

class Manager extends Employee {
  constructor(capability) {
    super(capability);
    this.empowerment = 3;
    this.jobTitle = 'Manager'
  }
}

class Director extends Employee {
  constructor(capability) {
    super(capability);
    this.empowerment = 5;
    this.jobTitle = 'Director'
  }
}

class Call {
  handler;
  handled;
  constructor(difficulty) {
    this.difficulty = difficulty;
  }
}

const c = new CallCentre()
c.hire(new Respondent(1))
c.dispatchCall(new Call(1))
c.hire(new Manager(1))
c.dispatchCall(new Call(3))