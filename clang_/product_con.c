#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PRODUCTS 100

struct Product {
    char name[50];
    float price;
    int quantity;
};

struct Product products[MAX_PRODUCTS];
int productCount = 0;

void addProduct() {
    if (productCount < MAX_PRODUCTS) {
        struct Product newProduct;
        printf("Enter product name: ");
        scanf("%s", newProduct.name);
        printf("Enter price: ");
        scanf("%f", &newProduct.price);
        printf("Enter quantity: ");
        scanf("%d", &newProduct.quantity);

        products[productCount++] = newProduct;
        printf("Product added successfully.\n");
    } else {
        printf("Product database is full.\n");
    }
}

void displayProducts() {
    printf("Product List:\n");
    for (int i = 0; i < productCount; i++) {
        printf("%d. Name: %s, Price: %.2f, Quantity: %d\n", i+1, products[i].name, products[i].price, products[i].quantity);
    }
}

void deleteProduct(int index) {
    if (index >= 0 && index < productCount) {
        for (int i = index; i < productCount - 1; i++) {
            products[i] = products[i + 1];
        }
        productCount--;
        printf("Product deleted successfully.\n");
    } else {
        printf("Invalid product index.\n");
    }
}

void editProduct(int index) {
    if (index >= 0 && index < productCount) {
        printf("Enter new price: ");
        scanf("%f", &products[index].price);
        printf("Enter new quantity: ");
        scanf("%d", &products[index].quantity);
        printf("Product information updated successfully.\n");
    } else {
        printf("Invalid product index.\n");
    }
}

int main() {
    int choice;
    do {
        printf("\n1. Add Product\n");
        printf("2. Display Products\n");
        printf("3. Delete Product\n");
        printf("4. Edit Product\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addProduct();
                break;
            case 2:
                displayProducts();
                break;
            case 3: {
                int index;
                printf("Enter index of product to delete: ");
                scanf("%d", &index);
                deleteProduct(index - 1);
                break;
            }
            case 4: {
                int index;
                printf("Enter index of product to edit: ");
                scanf("%d", &index);
                editProduct(index - 1);
                break;
            }
            case 5:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 5);

    return 0;
}

struct Product *products = NULL; // 동적 배열로 변경
int productCount = 0;
int capacity = 0; // 현재 용량
