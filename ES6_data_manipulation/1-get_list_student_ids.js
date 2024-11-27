function getListStudentIds(list) {
  if (Array.isArray(list)) {
    return list.map((students) => students.id);
  }

  return [];
}

export default getListStudentIds;
