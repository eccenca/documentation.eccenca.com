# Troubleshooting

Common deployment and configuration errors and the solutions to them.

## Error messages

### Project ‘CMEM’ not found

If the bootstrap data required for Corporate Memory has not been imported correctly, you will receive this message. If you are running the Docker Compose based deployment please double check the steps described in the README.

!!! note
    This step is handled automatically in the Ansible playbooks based deployment.

<figure markdown>
  ![22-1-error-message-project-not-found](22-1-error-message-project-not-found.png)
  <figcaption>Error message: CMEM not found</figcaption>
</figure>
