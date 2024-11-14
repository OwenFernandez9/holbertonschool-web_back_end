import Classroom from './0-classroom';

export function initializeRooms() {
  const rooms = [];
  Classroom.push(new Classroom(19));
  Classroom.push(new Classroom(20));
  Classroom.push(new Classroom(34));

  return rooms;
}
