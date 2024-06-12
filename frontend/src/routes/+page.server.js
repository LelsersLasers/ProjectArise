
export const load = async ({ url }) => {
	const restore = url.searchParams.get('back') != null;

	return {
		restore
	};
};