/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

/**
 * サーボモーターの方向を表す列挙型
 *
 * ```
 * _______________
 * ______  _______ straight
 * \ \______
 * \_______ curve
 * ```
 */
export enum PointDirection {
    STRAIGHT = 'straight',
    CURVE = 'curve',
}
