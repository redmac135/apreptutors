export type Subject = {
    pk: number;
    type: string;
    name: string;
}

export type Location = {
    pk: number;
    name: string;
    address: string;
}

export type Timeslot = {
    pk: number;
    weekday: string;
    start_time: string;
    instructor: {
        pk: number;
    };
    locations: number[];
}
export type SubjectTimeslot = {
    subjectId: number;
    timeslots: Timeslot[];
}