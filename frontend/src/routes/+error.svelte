<script>
    import { page } from '$app/stores';
</script>

<h1>ERROR</h1>

<p>Status: {$page.status}</p>
<p>Error message: {$page.error.message}</p>

<a href="/">
    <button>Back to Home</button>
</a>