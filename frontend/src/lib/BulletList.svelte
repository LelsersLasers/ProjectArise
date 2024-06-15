<script>
	export let content;

</script>

<style>
	ul {
		width: 85%;
        /* max-width: 300px; */
        margin: 0 auto;

        padding-left: 0;

        list-style: none;
        counter-reset: item;
	}
	li {
		margin-bottom: 10px;
	}
	li:before {
        content: "-";
        font-weight: bold;
        display: inline-block;
        margin-right: 10px;
    }
</style>



<ul>
	{#each content as item}
		<li>{item}</li>
	{/each}
</ul>