<script>
	import { goto } from '$app/navigation';

	export let data;

	data.label_display = data.label.replace('_', ' ');

	import { onMount } from 'svelte';

	onMount(() => {
		document.querySelector('html').style.backgroundColor = 'var(--bgGreen)';
	});

	function back() {
		goto('/?back');
	}
</script>

<style>
	h1 {
		text-align: center;
		text-transform: capitalize;
		font-style: italic;
		margin-top: 80px;
		margin-bottom: 50px;
		font-weight: normal;
	}

	h3 {
		text-align: center;
		text-decoration: underline;
		font-weight: normal;
	}

	ol {
		width: 100%;
		max-width: 300px;
		margin: 0 auto;

		padding-left: 0;

		list-style: none;
		counter-reset: item;
	}
	li {
		counter-increment: item;
		margin-bottom: 15px;
	}
	li:before {
		content: counter(item) ".) ";
		font-weight: bold;
		display: inline-block;
		margin-right: 10px;
	}

	.stickyFooter {
		position: fixed;
		left: 0;
		bottom: 0;
		background: var(--darkGreen);
		color: white;
		width: 97vw;

		margin-bottom: 2vw;
		margin-top: 3vw;
		margin-left: 1.5vw;
		margin-right: 1.5vw;
		border-radius: 20px;

		padding-top: 10px;
		padding-bottom: 10px;

		display: flex;
		justify-content: center;
		align-items: center;
		
		cursor: pointer;
	}
</style>

<svelte:head>
    <title>Project Arise | remove {data.label_display}</title>
</svelte:head>


<h1>{data.label_display}</h1>

<h3>HOW TO REMOVE</h3>

<ol>
	{#each data.remove_instructions as step, i}
		<li>{step}</li>
	{/each}
</ol>

<div class="stickyFooter zeroBottomMargin textAlignCenter" on:click={back}>
	Back
</div>