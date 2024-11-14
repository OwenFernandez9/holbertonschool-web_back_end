import Classroom from classroom

export function initializeRooms() {
    const array1 = new Classroom(19);
    const array2 = new Classroom(20);
    const array3 = new Classroom(34);

    return [array1, array2, array3]
}