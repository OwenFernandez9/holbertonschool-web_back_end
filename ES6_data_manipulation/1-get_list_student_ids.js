function getListStudentIds(list) {
    if (Array.isArray(list)){
        return list.map(students => students.id);
    }
    else {
        return [];
    }
}

export default getListStudentIds;