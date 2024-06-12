const FLASK_URL = "http://127.0.0.1:5000/";
// const FLASK_URL = "http://192.168.86.43:5000/";

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