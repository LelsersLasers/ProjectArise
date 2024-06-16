<script>
    export let content;

</script>

<style>
    ul {
        width: 85%;
        max-width: 300px;
        margin: 0 auto;

        padding-left: 0;

        list-style: none;
        counter-reset: item;

        padding-left: 18px;
    }
    @media (min-width: 768px) {
        ul {
            width: 50%;
            max-width: 50%;
        }
    }
    li {
        margin-bottom: 10px;
        position: relative;
        word-break: break-word;
    }
    li:before {
        position: absolute;
        vertical-align: middle;
        left: -16px;

        content: "-";
        font-weight: bold;
        display: inline-block;
        margin-right: 10px;
    }
</style>



<ul>
    {#each content as item}
        <li>{@html item}</li>
    {/each}
</ul>