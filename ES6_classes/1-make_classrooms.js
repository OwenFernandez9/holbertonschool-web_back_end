import ClassRoom from './0-classroom';

export function initializeRooms() {
  const rooms = [];
  ClassRoom.push(new ClassRoom(19));
  ClassRoom.push(new ClassRoom(20));
  ClassRoom.push(new ClassRoom(34));

  return rooms;
}
export default initializeRooms;