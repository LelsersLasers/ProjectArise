const FLASK_URL = 'https://projectarise.pythonanywhere.com/';
// const FLASK_URL = "http://64.98.192.13:3001/";
// const FLASK_URL = "http://localhost:3001/";

export const load = async ({ params }) => {
	const { label } = params;

	const url = FLASK_URL + "remove/" + label;
	const res = await fetch(url);
	const remove_instructions = await res.json();

	return {
		label,
		remove_instructions
	};
};